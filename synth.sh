# gain -5.6
for hz in 392 0 440; do  play "|sox -n -p synth .3 sin $hz";done
for hz in 165 196 247 165 196 247; do  play "|sox -n -p synth .3 sin $hz";done
