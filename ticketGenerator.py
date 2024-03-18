airline_name = 'AL1'
ticket_num = 100
toContinue = True
ticketList = []
def get_ticket_number(source, destination):
    global ticket_num
    ticket_num += 1
    return f"{airline_name}:{source[:3].upper()}:{destination[:3].upper()}:{ticket_num}"
while(toContinue):
    source=input('Enter Source: ')
    destination=input('Enter Destination: ')
    ticket_display = get_ticket_number(source, destination)
    ticketList.append(ticket_display)
    print(f"Your ticket number is: {ticket_display}")
    nextCommand = input("""Press c to continue | Press h for history: """)
    if(nextCommand == 'h'):
        print(f'Last 5 tickets: {', '.join(ticketList)}') 
    if(nextCommand == 'c' or nextCommand == 'h'):
        toContinue = True
    else:
        toContinue = False