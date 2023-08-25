# # Prep optimizer and scheduler
# optimizer = torch.optim.AdamW(
#     model.parameters(), lr=3e-4, betas=(0.9, 0.98), eps=1e-9, weight_decay=0.01
# )
# lr_lambda = lambda step: 1 - abs(2 * (step / total_training_steps) - 1)
# scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)
