# This function returns true, if iTunes is running.
on iTunesRunning()
	tell application "System Events" to (name of processes) contains "iTunes"
end iTunesRunning

# Check if iTunes is running.
# If iTunes is running, then run the itunescontroller python utility.
# If no face is detected, then probably the mac user is away, so pause playback.
# If a face is detected, then mac user is in front of the screen, so now if the playback is paused then start playing.
set playing to iTunesRunning()
if playing then
	set away to do shell script "itunescontroller"
	#display notification away
	if ((away as string) is equal to "no face") then
		tell application "iTunes" to pause
	else
		tell application "iTunes"
			set playerState to player state as string
			#display notification playerState
			if playerState is "paused" or playerState is "stopped" then
				play
			end if
		end tell
	end if
end if