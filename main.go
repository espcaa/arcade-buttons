package main

import (
	"github.com/stianeikeland/go-rpio/v4"
	"fmt"
	"os"
	"github.com/go-vgo/robotgo"
)

type arcade struct {
	LeftPin  rpio.Pin
	RightPin rpio.Pin
	DownPin  rpio.Pin
	PausePin rpio.Pin
	EnterPin rpio.Pin
}

func main() {
	if err := rpio.Open(); err != nil {
			fmt.Println(err)
			os.Exit(1)
		}
	defer rpio.Close()

	arcadeButtons := arcade{
		LeftPin:  rpio.Pin(5),
		RightPin: rpio.Pin(6),
		DownPin:  rpio.Pin(13),
		PausePin: rpio.Pin(19),
		EnterPin: rpio.Pin(26),
	}

	arcadeButtons.LeftPin.Input()
	arcadeButtons.RightPin.Input()
	arcadeButtons.DownPin.Input()
	arcadeButtons.PausePin.Input()
	arcadeButtons.EnterPin.Input()

	for {
		if arcadeButtons.LeftPin.Read() == rpio.Low {
			println("Left button pressed")
			robotgo.KeyTap("left")
		}
		if arcadeButtons.RightPin.Read() == rpio.Low {
			println("Right button pressed")
			robotgo.KeyTap("right")
		}
		if arcadeButtons.DownPin.Read() == rpio.Low {
			println("Down button pressed")
			robotgo.KeyTap("down")
		}
		if arcadeButtons.PausePin.Read() == rpio.Low {
			println("Pause button pressed")
			robotgo.KeyTap("escape")
		}
		if arcadeButtons.EnterPin.Read() == rpio.Low {
			println("Enter button pressed")
			robotgo.KeyTap("enter")
		}
		rpio.Delay(100 * rpio.Millisecond)
	}
}
