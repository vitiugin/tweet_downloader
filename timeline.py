import json
from searchtweets import collect_results, load_credentials, gen_request_parameters

search_args = load_credentials("twitter_keys.yaml", # config file
                                yaml_key="search_tweets_v2",
                                env_overwrite=False)

rule = gen_request_parameters("from:el_pais", # account name
                                start_time="2020-01-30", #UTC 2017-09-01 00:00
                                end_time="2020-01-31", #UTC 2017-10-30 00:00
                                tweet_fields="id,created_at,text", # comma-delimted list of Tweet JSON attributes wanted in endpoint responses
                                results_per_call=500, # maximum is 500
                                granularity=None)

tweets = collect_results(rule, max_tweets=500, result_stream_args=search_args)

with open('out.json', 'w') as outfile: # PATH to directory and name of the file
    outfile.write(str(json.dumps(tweets, indent=4, sort_keys=True)))
