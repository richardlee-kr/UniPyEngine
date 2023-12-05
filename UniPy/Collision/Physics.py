from ..Vector import *

class Physics:
    def __init__(self, targetScene):
        self.scene = targetScene

    '''
    TODO Check rotated collision
    AABB to OBB collision
    '''
    def OverlapCircleAll(self, point, radius, layer="Default"):
        allObjects = self.scene.hierarchy
        layered = list()
        detected = list()
        for object in allObjects:
            if object.layer == layer:
                if (object.transform.position - point).magnitude < 3*radius:
                    layered.append(object)
        
        del allObjects

        for object in layered:
            try:
                #if obejct has CircleCollider
                _radius = object.GetComponent("CircleCollider").radius
                _pos = object.GetComponent("CircleCollider").bounds.center + object.transform.position
                if (point-_pos).magnitude <= radius+_radius:
                    detected.append(object)
            except:
                try:
                    # else object has BoxCollider
                    objectPos = object.transform.position
                    boundSize = object.GetComponent("BoxCollider").bounds.size
                    testX = point.x
                    testY = point.y
                    if (point.x < objectPos.x-boundSize.x/2): testX = objectPos.x-boundSize.x/2
                    elif (point.x > objectPos.x+boundSize.x/2): testX = objectPos.x+boundSize.x/2
                    if (point.y < objectPos.y-boundSize.y/2): testY = objectPos.y-boundSize.y/2
                    elif (point.y > objectPos.y+boundSize.y/2): testY = objectPos.y+boundSize.y/2

                    distX = point.x-testX
                    distY = point.y-testY

                    distance = math.sqrt((distX*distX)+(distY*distY))

                    if(distance <= radius):
                        detected.append(object)
                except:
                    # no collider
                    continue

        return detected

    def OverlapBoxAll(self, point, size, layer="Default"):
        allObjects = self.scene.hierarchy
        layered = list()
        detected = list()
        for object in allObjects:
            if object.layer == layer:
                layered.append(object)

        del allObjects

        for object in layered:
            try:
                #if obejct has BoxCollider
                if (CheckShafts(object, point, size)):
                    detected.append(object)
            except:
                try:
                    # else object has CircleColldier
                    _radius = object.GetComponent("CircleCollider").radius
                    _pos = object.GetComponent("CircleCollider").bounds.center + object.transform.position
                    testX = _pos.x
                    testY = _pos.y
                    if (_pos.x < point.x-size/2): testX = point.x-size/2
                    elif (_pos.x > point.x+size/2): testX = point.x+size/2
                    if (_pos.y < point.y-size/2): testY = point.y-size/2
                    elif(_pos.y > point.y+size/2): testY = point.y+size/2

                    distX = _pos.x - testX
                    distY = _pos.y - testY
                    distance = math.sqrt((distX*distX)+(distY*distY))
                    if(distance <= _radius):
                        detected.append(object)
                except:
                    # no collider
                    continue

        return detected

def CheckShafts(obj, point, size):
    m_vector = obj.transform.position - point
    #print(m_vector)

    if(CheckShaft(obj, point, size/16, m_vector, obj.transform.right)): return False
    if(CheckShaft(obj, point, size/16, m_vector, obj.transform.up)): return False
    if(CheckShaft(obj, point, size/16, m_vector, Vector.right)): return False
    if(CheckShaft(obj, point, size/16, m_vector, Vector.up)): return False

    return True

def CheckShaft(obj, point, size, v, l):
    distance = abs(Vector.Dot(v,l))/16
    #print(distance)
    #print(abs(Vector.Dot(l,obj.transform.right)))
    #print(abs(Vector.Dot(l, obj.transform.right * obj.transform.scale.x * 0.5)))

    if (distance > abs(Vector.Dot(l, obj.transform.up * obj.transform.scale.y * 0.5))
        + abs(Vector.Dot(l, obj.transform.right * obj.transform.scale.x * 0.5))
        + abs(Vector.Dot(l, Vector.up * size * 0.5))
        + abs(Vector.Dot(l, Vector.right * size * 0.5))):
        #print("Has Shaft")
        return True