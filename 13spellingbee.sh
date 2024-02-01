#NYT Spellingbee
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "r" | grep -E "[rzoniac]{4,}" | grep -v "[bdefghjklmpqstuvwxy]"
