all : build

build : build_serv build_clnt 

build_serv:
	${MAKE} -C srv

build_clnt:
	# ${MAKE} -C clnt
	${MAKE} -C clnt2
	

clean:
	${MAKE} -C srv clean
	${MAKE} -C clnt clean
	${MAKE} -C clnt2 clean

run_serv:
	${MAKE} -C srv run

run_clnt:
	${MAKE} -C clnt2 run