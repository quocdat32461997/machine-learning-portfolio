from trainer import task

if __name__ == '__main__':
    args = task.get_args()
    task.train_and_evaluate(args)
