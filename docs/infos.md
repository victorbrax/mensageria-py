Adicione o caminho da sbin do RabbitMQ nas váriaveis de ambiente do Windows para
conseguir utilizar o plugin de management.

Exemplo de Path: C:\Program Files\RabbitMQ Server\rabbitmq_server-3.11.5\sbin

No Shell:
rabbitmq-plugins enable rabbitmq_management

Porta de acesso para configuração do Publisher:
localhost:5672 (in version 3.11: 15672 on browser)
Standard User: guest
Standard Password: guest

Conceitos rasos:
Publisher: Produtor
Exchange: Intercâmbio, porta de entrada das mensagens.
Queue: Filas de mensageria
Consumer: Consumidor
Routing Key: Chave para apontamento das Queues.