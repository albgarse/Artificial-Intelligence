# Red neuronal de Hopfield
# reconoce los caracteres 0,1 y 2

# transformar representación gráfica en valores -1 y +1
def graf_a_valores(datos):
  datos=datos.replace(' ', '') # quitar espacios
  salida=[]
  for i in range(len(datos)):
   if datos[i]=='.':
    salida.append(-1.0)
   else:
    salida.append(1.0)
  return salida

# transformar valores -1 y +1 a representación gráfica
def valores_a_graf(datos):
  salida=''
  cont=0
  for i in datos:
    cont=cont+1
    if i==-1.0:
      salida=salida+'.'
    else:
      salida=salida+'o'
    if cont%5==0:
      salida=salida+'\n' # salto de línea
  return salida


# calcula diferencial de energia
def denergia(linea):
  global n_entradas, pesos, nodos_entrada, sum_lin_pesos
  temp=0.0
  for i in range(n_entradas):
    temp=temp+(pesos[linea][i])*(nodos_entrada[i])
  return 2.0*temp-sum_lin_pesos[linea]


# devuelve el valor -1 o 1
def discretizar(n):
  if n<0.0:
    return -1.0
  else:
    return 1.0


# entrenamiento de la red
def entrenar(datos_ent):
  global n_entradas, pesos, nodos_entrada, sum_lin_pesos
  # actualizamos pesos
  for i in range(1,n_entradas):
    for j in range(i):
      for k in range(len(datos_ent)):
        datos=datos_ent[k]
        t=discretizar(datos[i])*discretizar(datos[j])
        temp=float(int(t+pesos[i][j])) # truncar decimales
        pesos[i][j]=temp
        pesos[j][i]=temp  # es una matriz simetrica

  # actualizamos suma de las líneas de la matriz de pesos
  for i in range(n_entradas):
    sum_lin_pesos[i]=0.0
    for j in range(i):
      sum_lin_pesos[i]=sum_lin_pesos[i]+pesos[i][j]


# clasificar patrón de entrada
def clasificar(patron, iteraciones):
  global n_entradas, pesos, nodos_entrada, sum_lin_pesos
  nodos_entrada=patron[:]
  for i in range(iteraciones):
    for j in range(n_entradas):
      if denergia(j)>0.0:
        nodos_entrada[j]=1.0
      else:
        nodos_entrada[j]=-1.0
  return nodos_entrada


if __name__ == '__main__':
  datos_ent = [
    graf_a_valores('.ooo. \
                    o...o \
                    o...o \
                    .ooo.'),

    graf_a_valores('.oo.. \
                    ..o.. \
                    ..o.. \
                    ..o..'),

    graf_a_valores('ooooo \
                    ...o. \
                    .o... \
                    ooooo')
  ]

  n_entradas=20  # número nodos en la red
  nodos_entrada=[0.0]*n_entradas
  sum_lin_pesos=[0.0]*n_entradas
  # crear matriz de pesos
  pesos=[]
  for id in range(n_entradas):
    pesos.append([0.0]*n_entradas)

  entrenar(datos_ent)
  # intentar reconocer el caracter distorsionado
  caracter=graf_a_valores('.oo.o \
                           ..o.. \
                           o.o.. \
                           ..o..')
  reconocido=clasificar(caracter, 5)

  print 'Caracter introducido:'
  print valores_a_graf(caracter)
  print 'Caracter reconocido:'
  print valores_a_graf(reconocido)

