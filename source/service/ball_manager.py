class BallManager: 

    def __init__(self):
        self.file_name = "ball_register.txt"

    def new_ball(self, ball_number):
        with open(self.file_name, "a") as file:
            file.writelines(f"{ball_number}\n")

    def get_all_balls(self):
        with open(self.file_name, "r") as file:
            balls = file.read().split('\n')
            balls = [ball for ball in balls if ball]
            return balls
        
    def clear_balls(self):
        with open(self.file_name, "w") as file:
            file.write('')