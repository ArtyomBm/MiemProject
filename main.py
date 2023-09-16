import obsws_python as obs
ws = obs.ReqClient(host="localhost", port=4465, password="123456")
ws1 = obs.EventClient(host='localhost', port=4465, password='123456')
cl = obs.ReqClient(host='192.168.0.152', port=4460, password="123456")
cl1 = obs.EventClient(host='192.168.0.152', port=4460, password="123456")
m = cl.get_scene_list()
n = {}
check = ws.get_scene_list()
def on_scene_collection_list_changed(data):
    ...
for i in range(len(check.scenes)):
    check.scenes[i].pop('sceneIndex')
for i in range(len(m.scenes)):
    m.scenes[i].pop('sceneIndex')
    n[i] = (m.scenes[i].values())
check1 = []
for i in range(len(check.scenes)):
    for j in check.scenes[i]:
        check1.append(check.scenes[i][j])
for i in range(len(m.scenes)):
    for j in m.scenes[i]:
        if not m.scenes[len(m.scenes)-1-i][j] in check1:
            ws.create_scene(m.scenes[len(m.scenes)-1-i][j])
t = ws.get_scene_list()
for i in range(len(t.scenes)):
    t.scenes[i].pop('sceneIndex')
    if not list(t.scenes[i].values())[0] in [j for e in list(n.values()) for j in e]:
        ws.remove_scene(list(t.scenes[i].values())[0])
p = {}
for i in range(len(m.scenes)):
    for j in m.scenes[i]:
        p[i] = m.scenes[i][j]
ws1.callback.register(on_scene_collection_list_changed)
cl1.callback.register(on_scene_collection_list_changed)
o = {}
for i in range(len(m.scenes)):
    o[i] = cl.get_scene_item_list(p[i])
for j in range(len(m.scenes)):
    for i in range(len(o[j].scene_items)):
        o[j].scene_items[i].pop('sceneItemTransform')
        o[j].scene_items[i].pop('sourceType')
        o[j].scene_items[i].pop('sceneItemLocked')
        o[j].scene_items[i].pop('sceneItemId')
        o[j].scene_items[i].pop('sceneItemEnabled')
        o[j].scene_items[i].pop('sceneItemIndex')
        o[j].scene_items[i].pop('sceneItemBlendMode')
        o[j].scene_items[i].pop('isGroup')
num = 0
"""for i in range(len(m.scenes)):
    count = len(o[i].scene_items)
    for j in range(count):
        for er in o[i].scene_items[j]:
            num+=1
            if not num%2 == 0:
                print(o[i].scene_items[j][er])
                ws.create_scene_item(p[i], o[i].scene_items[j][er])"""