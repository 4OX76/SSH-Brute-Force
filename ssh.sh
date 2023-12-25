#!/bin/bash


RED='\033[2;31m'  # if uname/passwd login found
GREEN='\033[0;32m' # if not login found
NC='\033[0m' 




function ssh(){
	NAME=$1		#USER-NAME
	PASSWD=$2	#PASSWD
	IP=$3		#Target IP-ADDRESS
	PORT=$4		#PORT

	sshpass -p $PASSWD ssh -o StrictHostKeyChecking=no $NAME@$IP -p $PORT hostname &> /dev/null
	
	if [ $(echo $?) -eq 0 ];then
		echo -e "${GREEN}[+]Name:$NAME\tPASSWORD:$PASSWD\tSUCCESS${NC}"
	else
			
		echo -e "${RED}[-]Name:$NAME\tPASSWORD:$PASSWD\tFAIL${NC}"
	fi
}

ssh $1 $2 $3 $4



