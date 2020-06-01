# Instrukcja instalacji podstawowej paczki

Zalecam skorzystanie z załączonego pliku pdf, gdzie poniższe zagadnienia są podane w wygodniejszej formie

## 1. Wymagane

Do obsługi tego oprogramowania zaleca się Ubuntu 16.04. Na tym systemie
operacyjnym można zagwarantować poprawność działania ROS Kinteic i node
Universal_Robots na dzień 06.04.2020r.
Ubuntu 18.04 i ROS Melodic powinien działać po wykonaniu następujących
kroków, ale nie jest to gwarantowane.


## 2. Instrukcja

1. ROS Kinetic

```
(a) Stworzyć testową paczkę za pomocą oprogramowania catkin
(b) Należy się posiłkować poradnikami Core ROS Tutorials punkty od
1.1 do 1.
(c) Pomocne mogą się okazać poradniki do ROS Catkin
```
2. Universal_robots

```
(a) Instalacja paczki Universal_robots
(b) Zalecam trzymać się instrukcji instalacji z ROS Wiki punkt 3. Insta-
lation
(c) W moim przypadku wystarczyło pobrać repozytorium za pomocą
apt-get, a potem ręcznie stworzyć bibliotekę w catkin.
```
3. Test

```
(a) Po instalacji należy sprawdzić, czy wszystko działa. Pomocny jest
filmik pokazujący połączenie 3 środowisk (w ostatnim kroku pojawia
się niepotrzebnie ur5 - wystarczy napisać ur3)
(b) Wymaga to otworzenia 3 terminali w trybie pracy z ros-em
source /opt/ros/kinetic/setup.bash
i rozpoczęcie
i. symulacji robota Listing 1
ii. konfiguracji robota Listing 2
iii. wizualizacji dla konfiguracji Listing 3
```

```
Listing 1: gazebo
```
roslaunch ur_gazebo ur3.launch

```
Listing 2: MoveIT
```
roslaunch ur3_moveit_config ur3_moveit_planning_execution.launch sim:=true

```
Listing 3: RViz
```
roslaunch ur3_moveit_config moveit_rviz.launch config:=true

