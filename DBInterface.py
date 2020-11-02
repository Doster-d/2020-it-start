import random
from simplite import Pylite
def generate_unique_number(already, row):
    num = random.randint(1, row)
    if num in already:
        num = generate_unique_number(already, row)
    return num

def generate_tasks(user_id, DB):
    tasks = list()
    random.seed(user_id)
    row = len(DB.get_items("Tasks"))
    already_in = list()
    for rand_id in range(50):
        rand_id = generate_unique_number(already_in, row)
        already_in.append(rand_id)
        tasks.append(DB.get_items("Tasks", "id={}".format(rand_id)))
    return tasks