from workflow.airline_workflow import AirlineWorkflow
import crewai.llms.cache as crewai_cache

crewai_cache.mark_cache_breakpoint = lambda msg: msg

workflow = AirlineWorkflow()


customer_request = input("Customer: ")

result = workflow.run(customer_request)

print("\nAssistant:")
print(result)