import simpy
import random

def bank(env, num_clients):
    for i in range(num_clients):
        yield env.timeout(random.expovariate(1))  # 客户到达时间间隔
        env.process(customer(env, i))

def customer(env, client_id):
    arrive_time = env.now
    print(f"Customer {client_id} arrives at {arrive_time}")

    with counter.request() as req:
        patience = random.uniform(1, 3)  # 耐心时间
        results = yield req | env.timeout(patience)

        wait_time = env.now - arrive_time

        if req in results:
            # 客户得到服务台资源
            serve_time = random.uniform(3, 5)  # 服务时间
            yield env.timeout(serve_time)
            leave_time = env.now
            print(f"Customer {client_id} served. Waited {wait_time:.2f} units. Leaves at {leave_time:.2f}")
        else:
            # 客户放弃服务
            print(f"Customer {client_id} reneged after {wait_time:.2f} units")

env = simpy.Environment()
counter = simpy.Resource(env, capacity=4)  # 增加4个服务台

env.process(bank(env, 10))
env.run()
