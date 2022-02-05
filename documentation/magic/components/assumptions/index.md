
# Assumptions component

The assumptions component allows you to easily sanity check your system, providing you with a
diagnostic tool, ensuring that your system is functioning as it should. An assumption is basically
an integration test, with one or more _"assumptions"_ about your system, which if not is true
implies your system is not functioning as it should. An example of an assumption can be for instance
as follows; _"If I try to login without a password the system should not authenticate me"_. Magic
is delivered out of the box with a whole range of integrated assumptions, but you can also create your own
assumptions from the _"Endpoints"_ menu item.

To create your own assumption open up your _"Endpoints"_ menu item, find an endpoint, invoke it
somehow, and create a new assumption after having invoked your endpoint. Below is a screenshot of this
process.

![Creating an assumption](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/new-assumption.jpg)

From your _"Assumptions"_ menu item you can easily execute all assumptions associated with your endpoints,
rapidly verifying as you change the state of your server that no change was applied that broke your
existing assumptions.

* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)
