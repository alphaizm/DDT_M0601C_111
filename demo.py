import usart
import time

port_name = "/dev/ttyAMA0"
# port_name = "/dev/serial0"
#port_name = "/dev/serial/by-id/PORTNAME"
cp = usart.CommunicationProtocol(port_name)

Speed = 0
Mode = 2
ID = 2
# ID = 1
Acce = 0
Brake_P = 0
# Speed, Mode, ID, Acce, Brake_P = 150, 2, 2, 0, 0

cp.Set_MotorID(ID)
cp.Set_MotorMode(Mode, ID)

# 0 ~ 330 まで20毎にカウントアップ
for i in range(-240, 240, 20):
    print(f'\n## Control_Motor Speed = {i}')
    Speed = i
    mode, Current, Velocity, Angle, Fault_value = cp.Control_Motor(Speed, ID, Acce, Brake_P)
    print('\tmode: '+ str(mode) + ' ' + 'Velocity ' + str(Velocity) + '(RPM/0.1ms) ' + 'Angle ' + str(Angle / 32767 * 360) + '(degree) ' + 'Fault_value ' + str(Fault_value))
    time.sleep(1)

    print('\t$$ Check_Motor')
    mode, Current, Velocity, Angle, Fault_value = cp.Check_Motor()
    print('\t\tmode: '+ str(mode) + ' ' + 'Velocity ' + str(Velocity) + '(RPM/0.1ms) ' + 'Angle ' + str(Angle / 32767 * 360) + '(degree) ' + 'Fault_value ' + str(Fault_value))
    time.sleep(1)


# Speed, Mode, ID, Acce, Brake_P = 0, 2, 1, 0, 0
Speed = 0

print('## Control_Motor')
mode, Current, Velocity, Angle, Fault_value = cp.Control_Motor(Speed, ID, Acce, Brake_P)
print('\tmode: '+ str(mode) + ' ' + 'Velocity ' + str(Velocity) + '(RPM/0.1ms) ' + 'Angle ' + str(Angle / 32767 * 360) + '(degree) ' + 'Fault_value ' + str(Fault_value))
time.sleep(1)

print('$$ Check_Motor')
mode, Current, Velocity, Angle, Fault_value = cp.Check_Motor()
print('\tmode: '+ str(mode) + ' ' + 'Velocity ' + str(Velocity) + '(RPM/0.1ms) ' + 'Angle ' + str(Angle / 32767 * 360) + '(degree) ' + 'Fault_value ' + str(Fault_value))
