-- This function returns true, if iTunes is running.
on iTunesRunning()
	tell application "System Events" to (name of processes) contains "iTunes"
end iTunesRunning

(* Check if iTunes is running.
If iTunes is running, then run the itunescontroller python utility.
If no face is detected, then probably the mac user is detection, so pause playback.
If a face is detected, then mac user is in front of the screen, so now if the playback is paused then start playing. *)

if iTunesRunning() then
	set detection to do shell script "/usr/local/bin/itunescontroller" as string
	tell application "iTunes"
		set playerState to player state as string
		if detection contains "no face" then
			if playerState is "playing" then
				display notification "No user in front of mac. iTunes will be paused."
				pause
			end if
		else
			if playerState is "paused" or playerState is "stopped" then
				display notification "Welcome back. iTunes will start playing."
				play
			end if
		end if
	end tell
end if
