build:
	docker network rm net_link -f
	docker network create -d overlay --attachable net_link
	docker build --network host -t getlink script

stack:
	docker stack deploy -c stack.yml example
	sleep 5

run-js: stop build stack
	docker run --rm -ti --network net_link getlink python3 get_links_js.py

run: stop build stack
	docker run --rm -ti  --network net_link getlink python3 get_links.py

stop:
	docker stack rm example
	sleep 10

