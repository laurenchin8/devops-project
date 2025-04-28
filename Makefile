
all:
	@echo "Nothing to do for all... hit specific targets"

build:
	@chmod +x build.sh
	./build.sh

test:
	@chmod +x test.sh
	./test.sh

lint:
	@chmod +x lint.sh
	./lint.sh

package:
	@chmod +x debBuild.sh
	./debBuild.sh
