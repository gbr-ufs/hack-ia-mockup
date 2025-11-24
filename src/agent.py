import mangaba
from mangaba import Process

chatbot = mangaba.Agent(role="Chatbot", goal="Help user", backstory="Chatbot")

help_user = mangaba.Task(
    description="{input}",
    expected_output="Friendly answer to the user's query",
    agent=chatbot,
)

crew = mangaba.Crew(
    agents=[chatbot], tasks=[help_user], process=Process.SEQUENTIAL, verbose=False
)
