# Python
This python script search for UserID and email in users.txt file, and print the results for all users that have both items and skip other users 

# Kubernetes
**Create Cluster**

$ minikube start 

**Add node to cluser**

$ minikube node add 

**get current nodes**

$ minikube kubectl get nodes 

**kubernetes API restricted**

$ kubectl proxy --port=8080 --accept-hosts='192\\.168\\.49\\.1$' --address=''192.168.49.1' & 

$ curl http://192.168.49.1/api/

**Deploy nginx ingress**

$ minikube addons enable ingress 

$ minikube addons enable ingress-dns

**verify nginx ingress status**

$ kubectl get namespace

**Add the `minikube ip` as a DNS server**

c:\ Add-DnsClientNrptRule -Namespace ".test" -NameServers "$(minikube ip)"

c:\ Get-DnsClientNrptRule | Where-Object {$_.Namespace -eq '.test'} | Remove-DnsClientNrptRule -Force; Add-DnsClientNrptRule -Namespace ".test" -NameServers "$(minikube ip)"

**Deploy "Juice Shop"**

kubectl create deployment juice-shop  --image=bkimminich/juice-shop

**Expose “Juice Shop” inside the cluster a service**

kubectl expose deployment juice-shop --type=NodePort --port=3000

**access Juice-Shop through  http://localhost:7080 port**

kubectl port-forward service/juice-shop 7080:3000

http://localhost:7080

**access Juice-Shop through  cluster ip**

minikube service juice-shop

http://192.168.228.95:30614


**Expose “Juice Shop” outside the cluster using the nginx ingress**

kubectl create ingress juice-shop-localhost --class=nginx --rule="juice-shop.localdev.me/*=juice-shop:3000"

kubectl port-forward --namespace=ingress-nginx service/ingress-nginx-controller 8080:80

http://juice-shop.localdev.me:8080
 
