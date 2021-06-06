EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr User 5906 5906
encoding utf-8
Sheet 1 1
Title "LEDuino Top Level"
Date "2021-06-05"
Rev "v0.01"
Comp ""
Comment1 "The basic layout involving the WeMos D1 Mini and MAX7219 LED Module."
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:Conn_01x05_Female J1
U 1 1 60BC38B4
P 3350 2450
F 0 "J1" H 3150 2900 50  0000 L CNN
F 1 "MAX7219_LED_Module" H 3150 2800 50  0000 L CNN
F 2 "" H 3350 2450 50  0001 C CNN
F 3 "~" H 3350 2450 50  0001 C CNN
	1    3350 2450
	1    0    0    -1  
$EndComp
$Comp
L MCU_Module:WeMos_D1_mini U1
U 1 1 60BC2196
P 2200 2300
F 0 "U1" H 2600 1700 50  0000 C CNN
F 1 "WeMos_D1_mini" H 2850 1600 50  0000 C CNN
F 2 "Module:WEMOS_D1_mini_light" H 2200 1150 50  0001 C CNN
F 3 "https://wiki.wemos.cc/products:d1:d1_mini#documentation" H 350 1150 50  0001 C CNN
	1    2200 2300
	1    0    0    -1  
$EndComp
Text Label 2200 3100 0    50   ~ 0
GND
Text Label 2100 1500 0    50   ~ 0
5V
Text Label 2600 2700 0    50   ~ 0
CS
Text Label 2600 2400 0    50   ~ 0
CLK
Text Label 2600 2600 0    50   ~ 0
DIN
Text Label 3150 2250 2    50   ~ 0
VCC
Text Label 3150 2350 2    50   ~ 0
GND
Text Label 3150 2450 2    50   ~ 0
DIN
Text Label 3150 2550 2    50   ~ 0
CS
Text Label 3150 2650 2    50   ~ 0
CLK
$EndSCHEMATC
