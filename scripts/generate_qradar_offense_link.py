import re


offenseid="-"

try:
  offenseid=re.findall('.*QRadar ID ([0-9]+) .*',str(incident.name))[0]
  incident.properties.qradar_offense_id=offenseid
  if incident.org_handle == "IBM":
    qradarurl="https://%s/console/qradar/jsp/QRadar.jsp?appName=Sem&pageId=OffenseSummary&summaryId=%s" % ("172.16.60.10", offenseid)
    incident.properties.qradar_links='''
        <a href="%s" target="_blank">%s</a>
    ''' % (qradarurl,"Offense Details")
    log.debug(qradarurl)
except:
  pass


