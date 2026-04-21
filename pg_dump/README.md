# Example pg_dump / Restore 

# pg_dumpall
```
pg_dumpall -h HOST -g --no-role-passwords --no-tablespaces -f all_roles.sql -U USERNAME
```

```
pg_dumpall -h HOST -U ADMINUSER -W -f output_pgdumpall -g --no-role-passwords --no-tablespaces -s
```

# pg_dump

```
pg_dump -v -h HOST -U bob -d postgres -Fd -C -j 10 -Z0 -f output_pg_dump
```

# pg_restore
```
psql -U ADMIN_NEW -d postgres -h HOST -f all_roles.sql
pg_restore -v -h HOST -U ADMINNEW -j 10 -C -d postgres output_pg_dump
```
