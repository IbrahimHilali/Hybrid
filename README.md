#About 
Hybrid Project with Python Language and Bootstrap. 

#USAGE
* you should at start only for one time run the command:
to avoid problem with postgres then you can use 
the normal docker-compose command:
```
docker-compose up db -d
``` 
```
docker-compose up -d
```
* create migration use django command:
```
docker-compose exec wdockeb python manage.py  'django command'
```
#License 
[MIT](LECENSE)
