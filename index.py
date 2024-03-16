from taipy.gui import Gui, notify
import taipy.gui.builder as tgb
from ls_stage_distribution import ls_stage_distribution_chart
from ls_trend import ls_trend_chart
from ls_stage_trend import ls_stage_trend_chart
from ls_peak_time import ls_peak_time_chart

with tgb.Page() as page:
    tgb.chart(figure="{ls_trend_chart}")
    tgb.chart(figure="{ls_stage_trend_chart}")
    tgb.chart(figure="{ls_peak_time_chart}")
    tgb.chart(figure="{ls_stage_distribution_chart}")

Gui(page).run(debug=True, use_reloader=True)
