import models
from app import app



################
### ALLINONE ###
################
@app.route('/addtemplate', methods=['GET', 'POST'])
def add_template():
    tasks = []
    tasks.append(models.SingleTask(
        task_name = 'bdf_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'ovl_file_upload', valueFalse = 'bdf_file_upload', dependentOnThisParameter = True),
        file_type = 'bdf',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['bdf=file.bdf'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'ovl_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'temperature_file_is_csv', valueFalse = 'ovl_file_upload', dependentOnThisParameter = True),
        file_type = 'ovl',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['ovl=file.ovl'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'temperature_file_is_csv',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'temperature_csv_upload', valueFalse = 'temperature_tdf_upload', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'temperature_csv_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'gdf_file', valueFalse = 'temperature_csv_upload', dependentOnThisParameter = True),
        file_type = 'csv',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['csv=file.csv', 'external_solver=no'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'temperature_tdf_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'external_solver', valueFalse = 'temperature_tdf_upload', dependentOnThisParameter = True),
        file_type = 'tdf',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['tdf=file.tdf'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'external_solver',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'sinas_maxdof', valueFalse = 'external_solver_false', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'external_solver_false',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['external_solver=no'],
        onlyAddIni = True,
        nextTask = 'gdf_file'
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'sinas_maxdof',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'sinas_maxdof_value', valueFalse = 'sinas_maxthn', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'sinas_maxdof_value',
        field_type = 'text',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'sinas_maxthn', valueFalse = 'sinas_maxdof_value', dependentOnThisParameter = True),
        addToIni = ['sinas_maxdof=$value'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'sinas_maxthn',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'sinas_maxthn_value', valueFalse = 'gdf_file', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'sinas_maxthn_value',
        field_type = 'text',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'gdf_file', valueFalse = 'sinas_maxthn_value', dependentOnThisParameter = True),
        addToIni = ['sinas_maxthn=$value'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'gdf_file',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'gdf_file_upload', valueFalse = 'ctl_file', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'gdf_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'ctl_file', valueFalse = 'gdf_file_upload', dependentOnThisParameter = True),
        file_type = 'gdf',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['gdf=file.gdf'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'ctl_file',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'ctl_file_upload', valueFalse = 'rbe2_conduction', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'ctl_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'rbe2_conduction', valueFalse = 'ctl_file_upload', dependentOnThisParameter = True),
        file_type = 'ctl',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['ctl=file.ctl'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'rbe2_conduction',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'rbe2_conduction_value', valueFalse = 'patran_out', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'rbe2_conduction_value',
        field_type = 'text',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'patran_out', valueFalse = 'rbe2_conduction_value', dependentOnThisParameter = True),
        addToIni = ['rbe2_conduction=$value'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'patran_out',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'final_task', valueFalse = 'patran_out_false', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'patran_out_false',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['patran_out=no'],
        onlyAddIni = True,
        nextTask = 'final_task'
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'final_task',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['gen=output', 'log=log.sil'],
        onlyAddIni = True,
        nextTask = 'run_pysinas'
        )
    )
    template = models.SinasJobTemplates(task = 'allinone', job_id = 'template', next_action = 'bdf_file_upload', template = tasks)
    template.save()
    return 'Done'




####################
### CONDUCTORGEN ###
####################
@app.route('/addtemplate', methods=['GET', 'POST'])
def add_template():
    tasks = []
    tasks.append(models.SingleTask(
        task_name = 'bdf_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'ovl_file_upload', valueFalse = 'bdf_file_upload', dependentOnThisParameter = True),
        file_type = 'bdf',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['bdf=file.bdf'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'ovl_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'ctl_file', valueFalse = 'ovl_file_upload', dependentOnThisParameter = True),
        file_type = 'ovl',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['ovl=file.ovl'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'ctl_file',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'ctl_file_upload', valueFalse = 'rbe2_conduction', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'ctl_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'rbe2_conduction', valueFalse = 'ctl_file_upload', dependentOnThisParameter = True),
        file_type = 'ctl',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['ctl=file.ctl'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'rbe2_conduction',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'rbe2_conduction_value', valueFalse = 'temperature_file_is_csv', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'rbe2_conduction_value',
        field_type = 'text',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'temperature_file_is_csv', valueFalse = 'rbe2_conduction_value', dependentOnThisParameter = True),
        addToIni = ['rbe2_conduction=$value'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'temperature_file_is_csv',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'temperature_csv_upload', valueFalse = 'temperature_tdf_upload', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'temperature_csv_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'glminfract', valueFalse = 'temperature_csv_upload', dependentOnThisParameter = True),
        file_type = 'csv',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['csv=file.csv', 'external_solver=no'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'temperature_tdf_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'external_solver', valueFalse = 'temperature_tdf_upload', dependentOnThisParameter = True),
        file_type = 'tdf',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['tdf=file.tdf'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'external_solver',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'glminfract', valueFalse = 'external_solver_false', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'external_solver_false',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['external_solver=no'],
        onlyAddIni = True,
        nextTask = 'glminfract'
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'glminfract',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'glminfract_value', valueFalse = 'gls_and_nds_output_file', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'glminfract_value',
        field_type = 'text',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'gls_and_nds_output_file', valueFalse = 'glminfract_value', dependentOnThisParameter = True),
        addToIni = ['glminfract=$value'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'gls_and_nds_output_file',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'sinas_maxdof_value', valueFalse = 'sinas_maxthn', dependentOnThisParameter = True),
        addToIni = ['gls=file.gds', 'nds=file.nco'],
        onlyAddIni = True,
        nextTask = 'sdf_file'
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'sdf_file_output',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'sdf_file_output_true', valueFalse = 'con_file_output', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'sdf_file_output_true',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['sdf=file.sdf'],
        onlyAddIni = True,
        nextTask = 'con_file'
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'con_file_output',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'con_file_output_true', valueFalse = 'run_pysinas', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'con_file_output_true',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['con=file.con'],
        onlyAddIni = True,
        nextTask = 'run_pysinas'
        )
    )
    template = models.SinasJobTemplates(task = 'conductorgen', job_id = 'template', next_action = 'bdf_file_upload', template = tasks)
    template.save()
    return 'Done'



###############
### CSV2TDF ###
###############
@app.route('/addtemplate', methods=['GET', 'POST'])
def add_template():
    tasks = []
    tasks.append(models.SingleTask(
        task_name = 'csv_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'agg_file', valueFalse = 'csv_file_upload', dependentOnThisParameter = True),
        file_type = 'csv',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['csv=file.csv', 'external_solver=no'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'agg_file',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'agg_file_upload', valueFalse = 'ctl_file', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'agg_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'ctl_file', valueFalse = 'agg_file_upload', dependentOnThisParameter = True),
        file_type = 'agg',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['agg=file.agg'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'ctl_file',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'ctl_file_upload', valueFalse = 'final_task', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'ctl_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'final_task', valueFalse = 'ctl_file_upload', dependentOnThisParameter = True),
        file_type = 'ctl',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['ctl=file.ctl'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'final_task',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['tdf=file.tdf', 'cas=file.cas'],
        onlyAddIni = True,
        nextTask = 'run_pysinas'
        )
    )
    template = models.SinasJobTemplates(task = 'csv2tdf', job_id = 'template', next_action = 'csv_file_upload', template = tasks)
    template.save()
    return 'Done'



####################
### GRADINTERPOL ###
####################
@app.route('/addtemplate', methods=['GET', 'POST'])
def add_template():
    tasks = []
    tasks.append(models.SingleTask(
        task_name = 'nsd_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'nco_file_upload', valueFalse = 'nsd_file_upload', dependentOnThisParameter = True),
        file_type = 'nsd',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['nsd=file.nsd'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'nco_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'ldf_file_upload', valueFalse = 'nco_file_upload', dependentOnThisParameter = True),
        file_type = 'nsd',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['nco=file.nco'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'ldf_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'tdf_file_upload', valueFalse = 'ldf_file_upload', dependentOnThisParameter = True),
        file_type = 'ldf',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['ldf=file.ldf'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'tdf_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'ctl_file', valueFalse = 'tdf_file_upload', dependentOnThisParameter = True),
        file_type = 'tdf',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['tdf=file.tdf'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'ctl_file',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'ctl_file_upload', valueFalse = 'sinas_maxdof', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'ctl_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'sinas_maxdof', valueFalse = 'ctl_file_upload', dependentOnThisParameter = True),
        file_type = 'ctl',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['ctl=file.ctl'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'sinas_maxdof',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'sinas_maxdof_value', valueFalse = 'sinas_maxthn', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'sinas_maxdof_value',
        field_type = 'text',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'sinas_maxthn', valueFalse = 'sinas_maxdof_value', dependentOnThisParameter = True),
        addToIni = ['sinas_maxdof=$value'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'sinas_maxthn',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'sinas_maxthn_value', valueFalse = 'final_task', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'sinas_maxthn_value',
        field_type = 'text',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'final_task', valueFalse = 'sinas_maxthn_value', dependentOnThisParameter = True),
        addToIni = ['sinas_maxthn=$value'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'final_task',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['gen=output', 'log=log.sil'],
        onlyAddIni = True,
        nextTask = 'run_pysinas'
        )
    )
    template = models.SinasJobTemplates(task = 'gradinterpol', job_id = 'template', next_action = 'nsd_file_upload', template = tasks)
    template.save()
    return 'Done'



################
### GRADPREP ###
################
@app.route('/addtemplate', methods=['GET', 'POST'])
def add_template():
    tasks = []
    tasks.append(models.SingleTask(
        task_name = 'bdf_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'ovl_file_upload', valueFalse = 'bdf_file_upload', dependentOnThisParameter = True),
        file_type = 'bdf',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['bdf=file.bdf'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'ovl_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'gdf_file_upload', valueFalse = 'ovl_file_upload', dependentOnThisParameter = True),
        file_type = 'ovl',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['ovl=file.ovl'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'gdf_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'tdf_file', valueFalse = 'gdf_file_upload', dependentOnThisParameter = True),
        file_type = 'gdf',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['gdf=file.gdf'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'tdf_file',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'tdf_file_upload', valueFalse = 'ctl_file', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'tdf_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'ctl_file', valueFalse = 'tdf_file_upload', dependentOnThisParameter = True),
        file_type = 'tdf',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['tdf=file.tdf'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'ctl_file',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'ctl_file_upload', valueFalse = 'rbe2_conduction', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'ctl_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'rbe2_conduction', valueFalse = 'ctl_file_upload', dependentOnThisParameter = True),
        file_type = 'ctl',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['ctl=file.ctl'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'rbe2_conduction',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'rbe2_conduction_value', valueFalse = 'final_task', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'rbe2_conduction_value',
        field_type = 'text',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'final_task', valueFalse = 'rbe2_conduction_value', dependentOnThisParameter = True),
        addToIni = ['rbe2_conduction=$value'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'final_task',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['nsd=file.nsd', 'nco=file.nco', 'ldf=file.ldf'],
        onlyAddIni = True,
        nextTask = 'run_pysinas'
        )
    )
    template = models.SinasJobTemplates(task = 'gradprep', job_id = 'template', next_action = 'bdf_file_upload', template = tasks)
    template.save()
    return 'Done'



###################
### INTERPOLATE ###
###################
@app.route('/addtemplate', methods=['GET', 'POST'])
def add_template():
    tasks = []
    tasks.append(models.SingleTask(
        task_name = 'sdf_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'con_file_upload', valueFalse = 'sdf_file_upload', dependentOnThisParameter = True),
        file_type = 'sdf',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['sdf=file.sdf'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'con_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'tdf_file_upload', valueFalse = 'con_file_upload', dependentOnThisParameter = True),
        file_type = 'con',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['con=file.con'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'tdf_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'ctl_file', valueFalse = 'tdf_file_upload', dependentOnThisParameter = True),
        file_type = 'tdf',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['tdf=file.tdf'],
        onlyAddIni = False,
        nextTask = None
        )
    )

    tasks.append(models.SingleTask(
        task_name = 'ctl_file',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'ctl_file_upload', valueFalse = 'sinas_maxdof', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'ctl_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'sinas_maxdof', valueFalse = 'ctl_file_upload', dependentOnThisParameter = True),
        file_type = 'ctl',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['ctl=file.ctl'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'sinas_maxdof',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'sinas_maxdof_value', valueFalse = 'sinas_maxthn', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'sinas_maxdof_value',
        field_type = 'text',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'sinas_maxthn', valueFalse = 'sinas_maxdof_value', dependentOnThisParameter = True),
        addToIni = ['sinas_maxdof=$value'],
        onlyAddIni = False,
        nextTask = None
        )
    )

    tasks.append(models.SingleTask(
        task_name = 'sinas_maxthn',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'sinas_maxthn_value', valueFalse = 'final_task', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'sinas_maxthn_value',
        field_type = 'text',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'final_task', valueFalse = 'sinas_maxthn_value', dependentOnThisParameter = True),
        addToIni = ['sinas_maxthn=$value'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'final_task',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['gen=output', 'log=log.sil'],
        onlyAddIni = True,
        nextTask = 'run_pysinas'
        )
    )
    template = models.SinasJobTemplates(task = 'interpolate', job_id = 'template', next_action = 'sdf_file_upload', template = tasks)
    template.save()
    return 'Done'



##############
### MATGEN ###
##############
@app.route('/addtemplate', methods=['GET', 'POST'])
def add_template():
    tasks = []
    tasks.append(models.SingleTask(
        task_name = 'bdf_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'ovl_file_upload', valueFalse = 'bdf_file_upload', dependentOnThisParameter = True),
        file_type = 'bdf',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['bdf=file.bdf'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'ovl_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'temperature_file_is_csv', valueFalse = 'ovl_file_upload', dependentOnThisParameter = True),
        file_type = 'ovl',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['ovl=file.ovl'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'temperature_file_is_csv',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'temperature_csv_upload', valueFalse = 'temperature_tdf_upload', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'temperature_csv_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'ctl_file', valueFalse = 'temperature_csv_upload', dependentOnThisParameter = True),
        file_type = 'csv',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['csv=file.csv', 'external_solver=no'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'temperature_tdf_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'ctl_file', valueFalse = 'temperature_tdf_upload', dependentOnThisParameter = True),
        file_type = 'tdf',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['tdf=file.tdf'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'ctl_file',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'ctl_file_upload', valueFalse = 'rbe2_conduction', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'ctl_file_upload',
        field_type = 'file',
        uploaded = models.Links(value = False, valueTrue = 'rbe2_conduction', valueFalse = 'ctl_file_upload', dependentOnThisParameter = True),
        file_type = 'ctl',
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['ctl=file.ctl'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'rbe2_conduction',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'rbe2_conduction_value', valueFalse = 'final_task', dependentOnThisParameter = True),
        addToIni = [],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'rbe2_conduction_value',
        field_type = 'text',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = 'final_task', valueFalse = 'rbe2_conduction_value', dependentOnThisParameter = True),
        addToIni = ['rbe2_conduction=$value'],
        onlyAddIni = False,
        nextTask = None
        )
    )
    tasks.append(models.SingleTask(
        task_name = 'final_task',
        field_type = 'bool',
        uploaded = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        file_type = None,
        value = None,
        valuePresent = models.Links(value = False, valueTrue = None, valueFalse = None, dependentOnThisParameter = False),
        addToIni = ['sdf=sdf_output.sdf', 'con=con_output.con'],
        onlyAddIni = True,
        nextTask = 'run_pysinas'
        )
    )
    template = models.SinasJobTemplates(task = 'matgen', job_id = 'template', next_action = 'bdf_file_upload', template = tasks)
    template.save()
    return 'Done'