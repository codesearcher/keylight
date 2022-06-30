#Developed by W. Calera /jun/2022
import bpy
import bmesh
#import time

def about():
 print('plano: index of functions')
 print('use dir(plano) to view')

def plane(planeName,row,col):
  a = del_all_vert(planeName)
  bpy.ops.object.mode_set(mode='EDIT')
  mesh = bpy.data.meshes.new('m')
  v = create_seq_vert(row,col);
  f = create_seq_faces(v,row,col);
  mesh.from_pydata(v,[],f); #step 5:
  mesh.update();    #link all this to the object
  bpy.ops.object.mode_set(mode='OBJECT')
  tmp=a.name;       #rename old object....
  a.name=a.name+'_old';
  b = bpy.data.objects.new(tmp,mesh) #and create a new
  #b.rotation_euler.order='XYZ';
  #b.rotation_euler.rotate_axis('Z',180); #rotates 180 degrees in z axis  
  bpy.context.scene.collection.objects.link(b) #add it to scene
  b.location=center_to_origin(b); #center it
  b.location[0]-=2.6; #sligth deslocate in x axis
  print('\rcriada a malha 3D')
  return b



def list_objs():
  print('objects in scene:');
  for o in bpy.context.scene.objects.items():
    print(o);

def center_to_origin(obj): #center obj to origin where:
  width = obj.dimensions[0] #obj is the object itself,
  height= obj.dimensions[1] #not the object name
  nw = width /2 #new width
  nh = height/2 #new height
  v = [-nw,-nh,0] #result vector
  return v

def create_seq_vert(row,col):
  v=[]    #step 3:create the vertices
  s = 0.5 #and positionating them
  for i in reversed(range(0,row)): 
    for j in (range(0,col)):
      v.append((i*s,j*s,0))
  return v

def create_seq_faces(v,row,col):
  f=[]  #step 4: create the faces
  for i in range(0,row-1): #create faces   4----3
    for j in range(0,col-1):              #|    |
      v1 = (i+1)*row+j   #vertex 1         1----2
      v2 = (i+1)*row+j+1 #vertex 2
      v3 = (i  )*row+j+1 #vertex 3
      v4 = (i  )*row+j   #vertex 4
      f.append((v1,v2,v3,v4))
  return f

def del_all_vert(objName): #etapa 2:deleta todos os vertices
  a = bpy.context.scene.objects[objName]
  bpy.ops.object.select_all(action='DESELECT')
  bpy.ops.object.mode_set(mode='OBJECT')
  for v in a.data.vertices:
    v.select=True;
  bpy.ops.object.mode_set(mode='EDIT')
  bpy.ops.mesh.delete(type='VERT')
  bpy.ops.object.mode_set(mode='OBJECT')
  print('deletou tudo...',end=':')
  return a

def set_vertexcolor(obj,vert,color): #object name , vertex number, color [r,g,b,a], material name
  try:
   D = bpy.data                     # mat with vertex color enabled in shader editor
   mat=D.objects[obj].data.materials[0].name;  #material already set
   if len(D.objects[obj].material_slots) < 1:
    # if there is no slot then we append to create the slot and assign
    D.objects[obj].data.materials.append(D.materials[mat])
   else:    # we always want the material in slot[0]
    D.objects[obj].material_slots[0].material = D.materials[mat]
   D.objects[obj].data.vertex_colors[0].data[vert].color.foreach_set(color)
   #bpy.ops.object.mode_set(mode='EDIT');
   #time.sleep(.001)
   #bpy.ops.object.mode_set(mode='OBJECT')
  except: pass;
  return vert

def get_vertexcolor(obj,vert):
  a=bpy.data.objects[obj] #an object
  c=[None]*4; # var color
  v=a.data.vertex_colors[0].data[vert].color.foreach_get(c); #an vertex
  return c;

def set_vertexcolorgroup(obj,vert,color,row_size):
  a=(vert//row_size);  #a=a*(row_size-1)*4-4*(a-1);
  a=-4*(a);
  try:
   b=set_vertexcolor(obj,(vert*4)-3+a,color);  
   c=set_vertexcolor(obj,(vert*4)  +a,color);           
   d=set_vertexcolor(obj,(vert*4)-6+4*row_size+a,color);  
   e=set_vertexcolor(obj,(vert*4)-1+4*row_size+a,color);
   #print(str(b)+','+str(c)+','+str(d)+','+str(e),end=' / ');#debug
  except e: pass;#print(e);

def get_vertexcolorgroup(obj,vert,row_size):
  a=(vert//row_size);
  a=-4*(a);
  c=[]
  try:
   c.append(get_vertexcolor(obj,(vert*4)-3+a));  
  except: pass;
  return c[0];

def moveVerticesRows(obj,col,row):
  a=bpy.context.scene.objects[obj]
  for i in reversed(range(1,row)): #atualiza/movimenta fileiras
   for j in range(0,col): #vertices dessa fileira
     v = a.data.vertices[i*col+j]; #pega vertice atual
     va= a.data.vertices[(i-1)*col+j]; #pega vertice da fileira anterior
     v.co[2]=va.co[2]*0.95 #vert atual recebe 95% da pos z do vert anterior

def moveObjectRows(obj_,fi,rows,cols=12): #move rows of objects obj_ represents obj1,obj2,...obj9
 for i in range(0,rows):          #rows: from front to back
  for j in range(0,cols):         #cols: from left to right
   idx=(i*cols)+(j)               #fi: actual row in first position
   a = bpy.context.scene.objects[obj_+str(idx)];  #pega objeto
   a.location.x+=-1.8-1.2*i
 move_p_1=(rows-fi) #fileira a voltar pra 1a posicao
 if move_p_1==rows: move_p_1=0
 for i in range(0,cols): 
   idx=(move_p_1*cols)+(i) 
   a = bpy.context.scene.objects[obj_+str(idx)] #pega objeto
   a.location.z=0
   a.location.x=0
 try:
   a.material_slots[0].material.diffuse_color[3]=0.5 #muda o alpha [r,g,b,a]
 except: pass
 return move_p_1 

def set_verticehigh(obj,i,msg,maxhigh): #brings objecto to the high (z axis)
 a = bpy.context.scene.objects[obj] #pega objeto
 v = a.data.vertices[i]; #pega vertice
 v1= a.data.vertices[i-1]; #pega vertice antes
 v2= a.data.vertices[i+1]; #pega vertice depois
 fat=msg.note/84;
 v.co[2] =maxhigh  *fat #
 if i-1>=0: v1.co[2]=maxhigh  *(fat/2) #
 if i+1<=23:v2.co[2]=maxhigh  *(fat/2) #  

def set_verticedown(obj,i,vel=0.25): #slowly descends the object
 a = bpy.context.scene.objects[obj] #pega objeto
 v = a.data.vertices[i]; #pega vertice
 v1= a.data.vertices[i-1]; #pega vertice antes
 v2= a.data.vertices[i+1]; #pega vertice depois
 v.co[2] -=vel
 v1.co[2]-=vel/2 #
 v2.co[2]-=vel/2 #  

def map_values(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)
    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def rainbow_color(i,total,offset=0): #the color on 'i' in a 'total' spectrum
 #if i+offset>total:
 x=(1/total)*(i+offset);
 r=round( 2.0*abs( ((x-1  ) % 1)-0.5 ) ,2); # equation of
 g=round( 2.0*abs( ((x-1/3) % 1)-0.5 ) ,2); # triangular
 b=round( 2.0*abs( ((x-2/3) % 1)-0.5 ) ,2); # wave
 return [r,g,b,1]

def changeColorAsc(obj):  #muda a cor de acordo com o espectro - ascendente
 #a=bge.logic.getSceneList()[0].objects.get('Cube'+str(i)) #pega objeto
 #m=a.meshes[0].materials[0] #material...
 a = bpy.context.scene.objects[obj]
 im=0 #indice do material
 r=a.material_slots[im].material.diffuse_color[0]
 g=a.material_slots[im].material.diffuse_color[1]
 b=a.material_slots[im].material.diffuse_color[2]
 print('cor:'+str(r)+','+str(g)+','+str(b)+',')
 if r==0 and g==0 and b==1: #se azul
   #a.material_slots[im].material.diffuse_color=[0,1,1,1] #deixe ciano
   a.active_material.diffuse_color = [0,1,1,1] #c
 elif r==0 and g==1 and b==1: #se ciano
   a.active_material.diffuse_color = [0,1,0,1] #c
 elif r==0 and g==1 and b==0: #se verde
   a.active_material.diffuse_color = [1,1,0,1] #c
 elif r==1 and g==1 and b==0: #se amarelo
   a.active_material.diffuse_color = [1,0.5,0,1] #c
 elif r==1 and g==0.5 and b==0: #se laranja
   a.active_material.diffuse_color = [1,0,0,1] #c
 elif r==1 and g==0 and b==0: #se vermelho
   a.active_material.diffuse_color = [1,0,1,1] #c
 elif r==1 and g==0 and b==1: #se violeta
   #a.material_slots[im].material.diffuse_color=[0,0,1,1] #deixe azul
   pass; #a.active_material.diffuse_color = [0,0,1,1] #c

def changeColorDesc(obj):  #muda a cor de acordo com o espectro - descendente
 a = bpy.context.scene.objects[obj]
 im=0 #indice do material
 al=0.5 #indice alfa
 r=a.material_slots[im].material.diffuse_color[0]
 g=a.material_slots[im].material.diffuse_color[1]
 b=a.material_slots[im].material.diffuse_color[2]
 print('cor:'+str(r)+','+str(g)+','+str(b)+',')
 if r==0 and g==0 and b==1: #se azul
   pass; #a.active_material.diffuse_color = [1,0,1,al] #c
 elif r==0 and g==1 and b==1: #se ciano
   a.active_material.diffuse_color = [0,0,1,al] #blue
 elif r==0 and g==1 and b==0: #se verde
   a.active_material.diffuse_color = [0,1,1,al] #cyan
 elif r==1 and g==1 and b==0: #se amarelo
   a.active_material.diffuse_color = [0,1,0,al] #green
 elif r==1 and g==0.5 and b==0: #se laranja
   a.active_material.diffuse_color = [1,1,0,al] #yellow
 elif r==1 and g==0 and b==0: #se vermelho
   a.active_material.diffuse_color = [1,0.5,0,al] #orange
 elif r==1 and g==0 and b==1: #se violeta
   a.active_material.diffuse_color = [1,0,0,al] #red

def set_material(ob,mat): #object name, material name
  D=bpy.data;
  bpy.ops.object.mode_set(mode = 'EDIT')
  if len(D.objects[ob].material_slots) < 1:
    # if there is no slot then we append to create the slot and assign
    D.objects[ob].data.materials.append(D.materials[mat])
  else:    # we always want the material in slot[0]
    D.objects[ob].material_slots[0].material = D.materials[mat]
  bpy.ops.mesh.select_all(action='SELECT');
  bpy.ops.object.material_slot_assign();
  bpy.ops.object.mode_set(mode = 'OBJECT')
  D.objects[ob].data.vertex_colors.new(); #bpy.ops.mesh.vertex_color_add();

def get_material(obj): #TO DO
  D=bpy.data;
  #print('material name:'+mat.name)
