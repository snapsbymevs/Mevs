"""Sync public Pixelfed images into photos.json. Requires PIXELFED_TOKEN if instance requires auth."""
import json, os, urllib.request, urllib.parse, html, re
BASE='https://pixelfed.social'; TOKEN=os.getenv('PIXELFED_TOKEN','')
def get(path):
    headers={'Accept':'application/json','User-Agent':'MEVS-portfolio-sync/1.0'}
    if TOKEN: headers['Authorization']='Bearer '+TOKEN
    req=urllib.request.Request(BASE+path,headers=headers)
    with urllib.request.urlopen(req,timeout=25) as r:return json.load(r)
acct=get('/api/v1/accounts/lookup?acct=mevs')
if not isinstance(acct,dict) or not acct.get('id'):raise RuntimeError('Account lookup unavailable')
photos=[]; max_id=None
for page in range(5):
    q={'limit':'80','only_media':'true','exclude_replies':'true'}
    if max_id:q['max_id']=max_id
    statuses=get('/api/v1/accounts/'+str(acct['id'])+'/statuses?'+urllib.parse.urlencode(q))
    if not statuses:break
    for s in statuses:
        if s.get('visibility')!='public' or s.get('sensitive'):continue
        caption=html.unescape(re.sub('<[^>]+>',' ',s.get('content',''))).strip()
        for media in s.get('media_attachments',[]):
            if media.get('type') not in ('image','photo'):continue
            url=media.get('url') or media.get('remote_url')
            if url:photos.append({'image':url,'alt':media.get('description') or caption or 'Photograph by MEVS','caption':caption[:110],'date':s.get('created_at','')[:10],'post_url':s.get('url')})
    max_id=statuses[-1]['id']
    if len(statuses)<80:break
if not photos:raise RuntimeError('No public photos returned; keeping existing data')
with open('photos.json','w') as f:json.dump(photos,f,ensure_ascii=False,indent=2)
print('Saved',len(photos),'photos')
