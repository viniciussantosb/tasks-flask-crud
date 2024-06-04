from flask import Flask, request, jsonify
from models.task import Task
# __name__ = __main__ se executado de forma manual e não importado por outro arquivo
# variavel name possui o valor "__main__" dentro dela 
app = Flask(__name__)

#CRUD   
# create, read, update and delete = criar, ler, atualizar e deletar 
# rota é comunicação, receba informações e devolva informações para o solicitante

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])  
def create_task():
    global task_id_control # para função ter acesso a variável
    
    #recuperar o que o cliente enviou
    data = request.get_json()

    new_task = Task(id=task_id_control,title=data['title'], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    return jsonify({'message': 'Nova tarefa criada com sucesso'})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
             }
    
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t

    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']

    return jsonify({"message": "Tarefa atualizada com sucesso"})

@app.route("/tasks/<int:id>", methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    
    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})

# debug para ver informaçoes rodando no servidor true
if __name__ == "__main__":
    app.run(debug=True) # recomendado para o desenvolvimento local