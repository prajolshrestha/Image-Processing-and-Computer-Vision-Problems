% Threshold-based Time series Segmentation

% learn: detrend, eval, cellfun, patch, bwconncomp

%% 

% generate smooth time series
N = 5000;
tv = (0:N-1)/(N/10);
ts = detrend(cumsum(randn(N,1))); %brownien noise

patchcolor = 'rg';
whichsign ='<>';


figure(1),clf,hold on
plot(tv,ts)
plot(get(gca,'xlim'),[0 0],'k--')

%% Find threshold of 10% on both tails of the distribution
tmpsort = sort(ts);

thresh(1) = tmpsort(round(.1*N));
thresh(2) = tmpsort(round(.9*N));

%% Segmentation: loop over the two threshold

for threshi = 1:2

    % find all the regions exceeding threshold
    eval([ 'beyondthresh = ts' whichsign(threshi) 'thresh(threshi);'])
    
    % get islands
    islands = bwconncomp(beyondthresh);

    % bonus: remove any island with fewer than 5 points
    islands.num = cellfun(@length,islands.PixelIdxList);
    islands2keep = islands.num > 4;
    islands.PixelIdxList = islands.PixelIdxList(islands2keep);
    islands.NumObjects = sum(islands2keep);

    %loop through and draw patches to 0
    for i = 1: islands.NumObjects

        %find xy points
        xpnts = tv(islands.PixelIdxList{i});
        ypnts = ts(islands.PixelIdxList{i});

        % draw the patch
        patch([xpnts xpnts(end:-1:1)],[zeros(1,length(ypnts)) ypnts(end:-1:1)'],patchcolor(threshi),'facealpha',.5,'linestyle','none');
    end


end










