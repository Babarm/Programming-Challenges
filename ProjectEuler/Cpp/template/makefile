SRC_DIR = ./src
INC_DIR = ../include
BUILD_DIR = ./bin

APP_NAME = run

CC = g++

CFLAGS = -O2 -std=c++11 -Wall -g
LFLAGS =
INCFLAGS = -I $(INC_DIR)

SOURCES = $(wildcard $(SRC_DIR)/*.cpp)
OBJECTS = $(SOURCES:$(SRC_DIR)/%.cpp=$(BUILD_DIR)/%.o)

all: $(APP_NAME)

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.cpp
	$(CC) $(CFLAGS) $(INCFLAGS) -o $@ -c $<

$(APP_NAME): $(OBJECTS)
	$(CC) $(LFLAGS) -o $@ $^

clean:
	rm -rf $(BUILD_DIR)/*.o

cleanall:
	rm -rf $(BUILD_DIR)/*.o $(APP_NAME)
