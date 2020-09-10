# find the incident to associate it with
incidents = helper.findIncidents(query_builder.equals(
    "id", "<replace this with an incident ID>").build())
# Take the result from querybuilder and associate the top incident with the email message
emailmessage.associateWithIncident(incidents[0])

# For each attachment in the email
for attachment in emailmessage.attachments:
    # Add an email attachment to incident
    incident.addEmailAttachment(attachment.id)