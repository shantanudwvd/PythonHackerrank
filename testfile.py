check_in=[]
check_out=[]
start_time=''
end_time=''
required=''
booked_slot=[]
def availability(check_in,check_out,start_time,end_time,required):
  if(abs(check_in[0]-start_time)>=required):
      if([start_time,check_in[0]] not in booked_slot):
          booked_slot.append([start_time,check_in[0]])
          return'slot is booked'
  if(abs(check_out[len(check_out)-1]-end_time)>=required):
      if ([check_out[len(check_out)-1],end_time] not in booked_slot):
          booked_slot.append([check_out[len(check_out)-1],end_time])
          return'slot is booked'
  for i in range(1,len(check_in)):
      if(check_in[i]-check_out[i-1]>=required):
          if([check_in[i],check_out[i-1]] not in booked_slot):
              booked_slot.append([check_in[i], check_out[i-1]])
              return'slot is booked'
  return'No free slot available'

print(availability(check_in,check_out,start_time,end_time,required))