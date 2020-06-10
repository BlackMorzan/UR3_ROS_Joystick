#!/bin/bash
# Instrukcje do wykonania przed uruchomieniem skryptu
# 1. Otwórz terminal, następnie w tle terminalu kliknij prawym przyciskiem myszy i wybierz opcje "Preferences"
# 2. Profiles -> Kliknij w istniejący profil -> Command Tab -> "When command exits" : zaznacz "Hold terminal open"
# 3. Przepisz nazwe profilu z lewej kolumny do zmiennej profil. 
# 	Np. profil ma nazwę "Unnamed" to zmienna profil=Unnamed


#zmienna profil przechowuje nazwe profilu terminala - należy ją zmienić!
profil=Unnamed

# W zależności od czasu otwarcia aplikacji należy zmienić czas sleep do swoich potrzeb.
gnome-terminal --window-with-profile=Unnamed -- roslaunch ur_gazebo ur3.launch
sleep 15s
gnome-terminal --window-with-profile=Unnamed -- roslaunch ur3_moveit_config ur3_moveit_planning_execution.launch sim:=true
sleep 10s
gnome-terminal --window-with-profile=Unnamed -- roslaunch ur3_moveit_config moveit_rviz.launch config:=true
