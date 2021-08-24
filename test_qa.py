import grpc
import argparse
import os

import jarvis_api.jarvis_nlp_core_pb2 as jcnlp
import jarvis_api.jarvis_nlp_core_pb2_grpc as jcnlp_srv
import jarvis_api.jarvis_nlp_pb2 as jnlp
import jarvis_api.jarvis_nlp_pb2_grpc as jnlp_srv


def get_args():
    parser = argparse.ArgumentParser(description="Jarvis Question Answering client sample")
    parser.add_argument("--jarvis-uri", type=str, help="URI to access Jarvis server")

    return parser.parse_args()


parser = get_args()

jarvis_uri = parser.jarvis_uri
if jarvis_uri is None:
    if "JARVIS_URI" in os.environ:
        jarvis_uri = os.getenv("JARVIS_URI")
    else:
        jarvis_uri = "localhost:50051"

grpc_server = jarvis_uri
channel = grpc.insecure_channel(grpc_server)
jarvis_nlp = jnlp_srv.JarvisNLPStub(channel)

req = jnlp.NaturalQueryRequest()

test_context = "In 2010 the Amazon rainforest experienced another severe drought, in some ways more extreme than the 2005 drought. The affected region was approximate 1,160,000 square miles (3,000,000 km2) of rainforest, compared to 734,000 square miles (1,900,000 km2) in 2005. The 2010 drought had three epicenters where vegetation died off, whereas in 2005 the drought was focused on the southwestern part. The findings were published in the journal Science. In a typical year the Amazon absorbs 1.5 gigatons of carbon dioxide; during 2005 instead 5 gigatons were released and in 2010 8 gigatons were released."
req.query = "How many tons of carbon are absorbed the Amazon in a typical year?"

req.context = test_context
resp = jarvis_nlp.NaturalQuery(req)
print(resp)
