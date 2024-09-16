def naira_converter(dollaramount):

	if dollaramount < 0:
		raise ValueError("Invalid dollar amount")
	
	EXCHANGERATE = 1550

	nigeria_naira = dollaramount * EXCHANGERATE

	return nigeria_naira

	