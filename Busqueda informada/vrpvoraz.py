# Heurística voraz para resolver TSP 
import math
from operator import itemgetter

def distancia(coord1, coord2):
  lat1=coord1[0]
  lon1=coord1[1]
  lat2=coord2[0]
  lon2=coord2[1]
  return math.sqrt((lat1-lat2)**2+(lon1-lon2)**2)

def en_ruta(rutas, c):
  ruta = None
  for r in rutas:
    if c in r:
      ruta = r
  return ruta

def peso_ruta(ruta):
  total=0
  for c in ruta:
    total = total + pedidos[c]
  return total


def vrp_voraz():
  # calcular lo ahorros
  s={}
  for c1 in coord:
    for c2 in coord:
      if c1 != c2:
        if not (c2,c1) in s:
          d_c1_c2 = distancia(coord[c1],coord[c2])
          d_c1_almacen = distancia(coord[c1], almacen)
          d_c2_almacen = distancia(coord[c2], almacen)
          s[c1,c2]= d_c1_almacen + d_c2_almacen - d_c1_c2
  # ordenar ahorros
  s=sorted(s.items(), key=itemgetter(1), reverse=True)

  # construir rutas
  rutas=[]
  for k,v in s:
    rc1 = en_ruta(rutas, k[0])
    rc2 = en_ruta(rutas, k[1])
    if rc1==None and rc2==None:
      # no están en ninguna rura. La creamos.
      if peso_ruta([k[0],k[1]]) <= max_carga:
        rutas.append([k[0],k[1]])
    elif rc1!=None and rc2==None:
      # ciudad 1 ya en una ruta. Agregamos la ciudad 2
      if rc1[0]==k[0]:
        if peso_ruta(rc1)+peso_ruta([k[1]]) <= max_carga:
          rutas[rutas.index(rc1)].insert(0, k[1])
      elif rc1[len(rc1)-1]==k[0]:
        if peso_ruta(rc1)+peso_ruta([k[1]]) <= max_carga:
          rutas[rutas.index(rc1)].append(k[1])
    elif rc1==None and rc2!=None:
      # ciudad 2 ya en una ruta. Agregamos la ciudad 1
      if rc2[0]==k[1]:
        if peso_ruta(rc2)+peso_ruta([k[0]]) <= max_carga:
          rutas[rutas.index(rc2)].insert(0, k[0])
      elif rc2[len(rc2)-1]==k[1]:
        if peso_ruta(rc2)+peso_ruta([k[0]]) <= max_carga:
          rutas[rutas.index(rc2)].append(k[0])
    elif rc1!=None and rc2!=None and rc1!=rc2:
      # ciudad 1 y 2 ya en una ruta. Tratamos de unirlas
      if rc1[0]==k[0] and rc2[len(rc2)-1]==k[1]:
        if peso_ruta(rc1)+peso_ruta(rc2) <= max_carga:
          rutas[rutas.index(rc2)].extend(rc1)
          rutas.remove(rc1)
      elif rc1[len(rc1)-1]==k[0] and rc2[0]==k[1]:
        if peso_ruta(rc1)+peso_ruta(rc2) <= max_carga:
          rutas[rutas.index(rc1)].extend(rc2)
          rutas.remove(rc2)

  return rutas


if __name__ == "__main__":
  coord = {
    'Malaga':(36.43, -4.24),
    'Sevilla':(37.23, -5.59),
    'Granada':(37.11, -3.35),
    'Valencia':(39.28, -0.22),
    'Madrid':(40.24, -3.41),
    'Salamanca':(40.57, -5.40),
    'Santiago':(42.52, -8.33),
    'Santander':(43.28, -3.48),
    'Zaragoza':(41.39, -0.52),
    'Barcelona':(41.23, +2.11)
    }

  pedidos = {
    'Malaga':10,
    'Sevilla':13,
    'Granada':7,
    'Valencia':11,
    'Madrid':15,
    'Salamanca':8,
    'Santiago':6,
    'Santander':7,
    'Zaragoza':8,
    'Barcelona':14
  }

  almacen = (40.23, -3.40)
  max_carga = 40

  rutas = vrp_voraz()
  for ruta in rutas:
    print ruta




