# agai
artificial intelligence course at AG

## perceptron - konfigurace

Samuel Soukup:
- 18.2.2019: edges, edges90, edges180, edges270 :0.7905050505050505, 53.5s 2.6GHz i7-3720QM 
- 25.2.2019: edges, edges90, edges180, edges270, hoes: 0.8084848484848485, 96.3s 2.6GHz i7-3720QM
- 4.3.2019: edges, edges90, edges180, edges270, black_features, nwhite_features, top_heavy;  perceptron: 0.957995799579958, 839s 2.6GHz i7-3720QM
- 12.3.2019: black_features, edges, edges90, edges180, edges270, joints, perceptron: 0.9601960196019602, 578.6s, 2.6GHz i7-3720QM
Jiri Laska:
- 18.2.2019: edges, hedges - 0.76
- 4.3.2019: edges, hedges; perceptron - +- 0.907

## návody:
### git
- TODO
### tensorflow
- instalace starsi verze kompatibilni se skolnimi pocitaci: 

```
 pip3 install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.5.1-cp36-cp36m-linux_x86_64.whl
```

- instalace aktualni verze na novych pocitacich:

```
pip3 install tensorflow
```

### pytorch
-instalace: 

```
pip3 install pytorch
```
## užitečné knihovny pro python
OpenCV: počítačové vidění, zpracování obrazu, jednoduché algoritmy nad obrázky a videem.
Neuronové sítě: keras (nejjednodušší), tensorflow (nejsložitější), pytorch (kompromis)
starší strojové učení: scikit-learn
