while True:
	try:
		num = int(input("Enter a number: "))
		break
	except ValueError:
		print('Thats\'s not a valid number')
	except KeyboardInterrupt:
		print('No input taken')
		break
	finally:
		print('\nAttempted Input\n')
