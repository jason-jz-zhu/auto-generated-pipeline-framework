


def generate_loader_stmt(targets):
    targets_str = ""

    for target in targets:
        if target["type"] == "orc":
            targets_str += "{}.write.format(\"{}\").mode(\"{}\").save((\"{}\"))\n".format(target["name"], target["type"], target["mode"], target["path"])
        elif target["type"] == "postgres":
            targets_str += "{}.write.format(\"jdbc\").mode(\"{}\").option(\"url\", \"jdbc:postgresql://{}:{}/{}\").option(\"dbtable\", \"{}\").option(\"user\", \"{}\").option(\"password\", \"{}\").option(\"driver\", \"org.postgresql.Driver\").save()\n".format(target["name"], target["mode"], target["host"], target["port"], target["database"], target["table"], target["user"], target["password"])
        elif target["type"] == "bigquery":
            print("bigquery: have not yet implemented, will do soon!!!")
        elif target["type"] == "mssql":
            print("mssql: have not yet implemented, will do soon!!!")
        elif target["type"] == "mysql":
            print("mysql: have not yet implemented, will do soon!!!")
        elif target["type"] == "mft":
            print("mft: have not yet implemented, will do soon!!!")
        elif target["type"] == "mongo":
            print("mongo: have not yet implemented, will do soon!!!")
        elif target["type"] == "elastic search":
            print("elastic search: have not yet implemented, will do soon!!!")
        elif target["type"] == "cassandra":
            print("cassandra: have not yet implemented, will do soon!!!")
        elif target["type"] == "oracle":
            print("oracle: have not yet implemented, will do soon!!!")
        else:
            print("{}: have not yet implemented, will do soon!!!".format(target["type"]))

    return targets_str
    