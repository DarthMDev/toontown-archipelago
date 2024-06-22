
export SERVICE_TO_RUN=UD
cd game

while true;
do 
    # launch the unix executable
    ./launch \ 
    --base-channel 1000000 \
    --max-channels 999999 \
    --stateserver 4002 \
    --astron-ip 127.0.0.1:7199 \
    --eventlogger-ip 127.0.0.1:7197 \
    config/common.prc \
    config/production.prc 


    sleep 5
done

