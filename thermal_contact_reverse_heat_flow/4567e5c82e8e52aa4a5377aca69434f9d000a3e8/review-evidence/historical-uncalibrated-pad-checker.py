"""Independent final-video check of exposed insulating-pad tops in every frame."""
from pathlib import Path
import json,subprocess,hashlib
import numpy as np
R=Path(__file__).resolve().parent;n='thermal_contact_reverse_heat_flow';root=R/'backups/thermal-pad-formal-v1'/n;records=[]
def project(m,p,i):
 eye=np.array(m['camera']['pos'],float);eye[0]+=.025*i/119;look=np.array(m['camera']['lookat'],float);forward=look-eye;forward/=np.linalg.norm(forward);right=np.cross(forward,[0,0,1]);right/=np.linalg.norm(right);up=np.cross(right,forward);v=np.array(p)-eye;scale=2048*48/36/np.dot(v,forward);return round(1024+np.dot(v,right)*scale),round(1024-np.dot(v,up)*scale)
for mf in sorted(root.glob('*/metadata.json')):
 m=json.loads(mf.read_text());p=m['phenomenon_data']['scene_params']
 for branch in ['true','counterfactual']:
  video=mf.parent/m['paths'][branch]['video'];state=dict(np.load(mf.parent/m['paths'][branch]['trajectory']));proc=subprocess.Popen(['ffmpeg','-v','error','-threads','1','-i',str(video),'-f','rawvideo','-pix_fmt','rgb24','pipe:1'],stdout=subprocess.PIPE);means=[];failures=[]
  for i in range(120):
   raw=proc.stdout.read(2048*2048*3);assert len(raw)==2048*2048*3;im=np.frombuffer(raw,np.uint8).reshape(2048,2048,3)
   frame=[]
   for j in range(2):
    center=(-1 if j==0 else 1)*(p['width']/2+state['gap'][i]/2)
    for dx in [-.2,.2]:
     x,y=project(m,(center+dx*p['width'],-.377,.78),i);rgb=im[y,x].astype(float);frame.append(rgb.tolist())
     if not (rgb[0]-rgb[2]>8 and rgb[1]-rgb[2]>6):failures.append(dict(frame=i,block=j,point_offset=dx,xy=[x,y],rgb=rgb.tolist()))
   means.append(frame)
  assert not proc.stdout.read(1);assert proc.wait()==0
  records.append(dict(case_id=m['task_id'],head_sha=m['generation']['git'],branch=branch,source_sha256=hashlib.sha256(video.read_bytes()).hexdigest(),samples=means,failures=failures))
output=R/'2026-10-12_thermal-pad-pixels.json';output.write_text(json.dumps(dict(status='PASS' if len(records)==4 and all(not r['failures'] for r in records) else 'FAIL',method='Read independently projected exposed pad-top pixels at four sample positions for all120 decoded native frames per video; verify beige pad material stays visible instead of alternating with gray tabletop. Actual bounds contact tested separately. No generator imports.',records=records),indent=2));print([(r['case_id'],r['branch'],len(r['failures'])) for r in records]);assert len(records)==4 and all(not r['failures'] for r in records)
