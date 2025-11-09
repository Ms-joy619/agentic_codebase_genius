walker main {
    has string: repo_url;

    can run {
        log "Starting Codebase Genius for " + self.repo_url;
        spawn -> supervisor(repo_url=self.repo_url);
    }
}
