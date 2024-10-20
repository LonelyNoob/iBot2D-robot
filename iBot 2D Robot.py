class Robot:
    def __init__(self,x=0,y=0):
        #Initialize the position of the robot at a point defined by the user or (0,0) by default
        self.x = x
        self.y = y
    def move_north(self):
        self.y += 1         #move up (North) by increasing y-coordinate by 1
    def move_south(self):
        self.y -= 1         #move down (South) by decreasing y-coordinate by 1
    def move_east(self):
        self.x += 1         #move to the right (East) by increasing x-coordinate by 1
    def move_west(self):
        self.x -= 1         #move to the left (West) by decreasing x-coordinate by 1
    

    def processing_commands(self, commands):
        # Process a sequence of commands and move the robot accordingly
        for command in commands:
            if command == 'N':
                self.move_north()
            elif command == 'S':
                self.move_south()
            elif command == 'E':
                self.move_east()
            elif command == 'W':
                self.move_west()    

    def get_position(self):
        # Return the robot's final position
        return (self.x, self.y)

x = int(input('Enter initial x-coordinate of robot:'))
y = int(input('Enter initial y-coordinate of robot:'))

robot=Robot(x,y)
#Creating a robot(object) with user defined initial coordinates

commands = input("Enter commands (N, S, E, W): ").upper() 
#Enter the sequence of commands (For eg. NSSEEWW)

robot.processing_commands(commands) 
#Process the commands to move the robot

#Get and display the final position of the robot
fin_pos = robot.get_position()
print(f"The robot's final position is: {fin_pos}")