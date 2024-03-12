import logging
import azure.functions as func

app = func.FunctionApp()

@app.schedule(schedule="0 0 12 * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def publish_rolx_stats(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')