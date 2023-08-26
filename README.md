# lr_schedules

This project currently just contains `LinearScheduler`, for custom linear learning rate schedules.


```python
from lr_schedules import LinearScheduler
import matplotlib.pyplot as plt
import torch
```

## PyTorch example, triangle


```python
times = [0, 0.5, 1]
values = [0, 1, 0]

W = torch.tensor([1.0], requires_grad=True)
optimizer = torch.optim.SGD([W], lr=0.1)
linear_scheduler = LinearScheduler(times, values, total_training_steps=100)
scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, linear_scheduler)

lr_vals = []
for step in range(100):
    optimizer.zero_grad()
    loss = torch.sum(W**2)
    loss.backward()
    optimizer.step()
    scheduler.step()
    lr_vals.append(optimizer.param_groups[0]["lr"])

plt.figure(figsize=(5, 2))
plt.plot(lr_vals)
plt.xlabel("Training step")
plt.ylabel("Learning rate")
plt.show()
```


    
![png](README_files/README_3_0.png)
    


## Pytorch example, ramp up and down


```python
times = [0, 0.1, 0.9, 1]
values = [0, 1, 0.9, 0]

W = torch.tensor([1.0], requires_grad=True)
optimizer = torch.optim.SGD([W], lr=0.1)
linear_scheduler = LinearScheduler(times, values, total_training_steps=100)
scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, linear_scheduler)

lr_vals = []
for step in range(100):
    optimizer.zero_grad()
    loss = torch.sum(W**2)
    loss.backward()
    optimizer.step()
    scheduler.step()
    lr_vals.append(optimizer.param_groups[0]["lr"])

plt.figure(figsize=(5, 2))
plt.plot(lr_vals)
plt.xlabel("Training step")
plt.ylabel("Learning rate")
plt.show()
```


    
![png](README_files/README_5_0.png)
    


## Pytorch example, specifying absolute number of steps


```python
times = [0, 12, 90, 100]
values = [0, 1, 0.8, 0]

W = torch.tensor([1.0], requires_grad=True)
optimizer = torch.optim.SGD([W], lr=0.1)
linear_scheduler = LinearScheduler(times, values)
scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, linear_scheduler)

lr_vals = []
for step in range(100):
    optimizer.zero_grad()
    loss = torch.sum(W**2)
    loss.backward()
    optimizer.step()
    scheduler.step()
    lr_vals.append(optimizer.param_groups[0]["lr"])

plt.figure(figsize=(5, 2))
plt.plot(lr_vals)
plt.xlabel("Training step")
plt.ylabel("Learning rate")
plt.show()
```


    
![png](README_files/README_7_0.png)
    


## Dev set up of repo

- Clone the repo
- Install `poetry` (repo was run with python3.9)
- Run `poetry install --with docs`
- Run `poetry run pre-commit install`
