<img src="../../img/logo.png" alt="Chmurowisko logo" width="200" align="right">
<br><br>
<br><br>
<br><br>

# DLA INSTRUKTORA

### NIE KOPIOWAĆ DO MATERIAŁÓW!

#### Do wykonania tego laboratorium potrzebe są następujące elementy:

**Image dockerowy uruchamianej aplikacji Mario.**
Jeśli nie ma obrazu na koncie AWS to trzeba go tam 

Obraz dostępny jest na docker hub pod adresem: https://hub.docker.com/r/kaminskypavel/mario

1. Pobrać obraz z docker hub:

```she
docker pull kaminskypavel/mario
```

2. Na koncie AWS w usłudze ECR utworzyć nowe repozytorium o nazwie **mario**

```she
aws ecr create-repository --repository-name mario
```

3. Z autentykować swojego klienta w ECR i potem wkleić jeszcze raz to co wypluje poniższa komenda

```shell
aws ecr get-login --no-include-email --region eu-west-1
```

3. Otagować aby wypchnąć do repozytorium

```she
docker tag kaminskypavel/mario 094104221953.dkr.ecr.eu-west-1.amazonaws.com/mario:latest
```

4. Wypchnać obraz do repozytorium:

```she
docker push 094104221953.dkr.ecr.eu-west-1.amazonaws.com/mario:latest
```

DONE!

**TODO**: Zrobić kiedyś poprostu tamplate cloudformation na ten kawałek.

Masz kwant czasu? Nie krępuj się 

<br><br>

<center><p>&copy; 2019 Chmurowisko Sp. z o.o.<p></center>